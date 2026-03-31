from base.log import logger

class Asert:
    @staticmethod
    def asert_contrast(code, data, status_code, result_data):
        """验证code和响应数据,可验证项或两项"""
        # 预期结果code和data都填写时
        if code and data:
            logger.info("进行验证code、data:\n预期返回:"+str(code)+"\t\t\t实际返回:"+str(status_code))
            logger.info("进行验证data、result_data: \n预期返回:"+str(data) +"\t\t\t实际返回:"+str(result_data))
            try:
                # 断言状态码
                assert code == status_code, f"状态码不匹配: 预期{status_code}, 实际{code}"
                # 断言响应数据
                assert data in result_data, f"响应数据不匹配: 预期包含{data}, 实际{result_data}"
                logger.info("验证通过")
                return True  # ✅ 关键修复：断言成功时返回True
            except AssertionError as e:
                logger.warning("断言失败:"+ str(e))
                return False
        # 仅验证状态码的情况
        elif code:
            logger.info("进行验证code:\n预期返回:"+str(status_code)+"\t\t\t实际返回:"+str(code))
            try:
                assert code == status_code, f"状态码不匹配: 预期{status_code}, 实际{code}"
                logger.info("验证通过")
                return True  # ✅ 关键修复：断言成功时返回True
            except AssertionError as e:
                logger.warning("断言失败:"+ str(e))
                return False
        # 仅验证响应数据的情况
        elif data:
            logger.info("进行验证data:\n预期返回:"+str(data)+"\t\t\t实际返回:"+str(result_data))
            try:
                assert data in result_data, f"响应数据不匹配: 预期包含{data}, 实际{result_data}"
                logger.info("验证通过")
                return True  # ✅ 关键修复：断言成功时返回True
            except AssertionError as e:
                logger.warning("断言失败:"+ str(e))
                return False
        # 无验证项的情况
        else:
            logger.warning("无验证项，跳过断言")
            return True