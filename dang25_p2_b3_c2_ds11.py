import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang25_p2_b3_c2_ds11(self):
            # Khai báo biến
            # Định dạng số nguyên thành chuỗi có dấu chấm phân cách hàng nghìn
            def fmt(num):
                return "{:,}".format(int(round(num))).replace(",", ".")


            # --- B3: KHAI BÁO VÀ NGẪU NHIÊN HÓA CÁC THAM SỐ ---
            L1 = random.choice([3200000, 6000000, 6400000, 9600000])  # Lương bậc 1
            q_bac = 1.25  # Tăng 25% mỗi bậc

            L4 = L1 * (q_bac**3)  # Lương bậc 4
            L5 = L1 * (q_bac**4)  # Lương bậc 5
            L7 = L1 * (q_bac**6)  # Lương bậc 7

            tong_nam = random.choice([27, 30, 33])  # Tổng số năm làm việc
            nam_vuot_khung = tong_nam - 21  # Số năm vượt khung (7 bậc * 3 năm = 21 năm)
            q_vk = 1.01  # Tăng 1% mỗi năm vượt khung

            # Tổng tiền lương 21 năm đầu
            T21 = 36 * L1 * (q_bac**7 - 1) / (q_bac - 1)

            # Tổng tiền lương các năm vượt khung
            L_vk_1 = L7 * q_vk
            T_vk = 12 * L_vk_1 * (q_vk**nam_vuot_khung - 1) / (q_vk - 1)

            # Tổng tiền lương cả quá trình
            T_tong = T21 + T_vk

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (
                "Anh Bình là nhân viên của một công ty A. Từ ngày 1/2/2026 anh Bình được nâng lương lên bậc 4, "
                "mức lương anh hiện hưởng là %s đồng mỗi tháng. Theo quy định của công ty, nếu không bị kỷ luật, "
                "không có khen thưởng đặc biệt thì cứ sau 3 năm anh Bình sẽ được nâng một bậc lương, tăng thêm 25\\%% "
                "so với bậc lương trước, tối đa là bậc 7. Khi hết bậc 7 sẽ chuyển sang vượt khung. Lương vượt khung năm sau "
                "cao hơn năm trước 1\\%% và vẫn nhận hàng tháng. Lương bậc 1 sẽ được tính sau khi hết đúng 1 năm tập sự. "
                "Anh Bình là người rất nghiêm túc, không vi phạm kỷ luật. Anh dự định sẽ làm việc %s năm ở công ty này rồi nghỉ hưu."
                % (fmt(L4), tong_nam)
            )

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = "\\True Lương bậc 1 của anh Bình là %s đồng" % (fmt(L1))
            nb_da_1_s = "Lương bậc 1 của anh Bình là %s đồng" % (fmt(L1 + 500000))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = (
                "Vì cứ sau 3 năm mức lương tăng 25\\%% ($q = 1,25$) nên lương bậc 4 liên hệ với lương bậc 1 theo công thức: \\\\"
                "$L_4 = L_1 \\cdot 1,25^3 \\Rightarrow L_1 = \\frac{%s}{1,25^3} = %s$ đồng."
                % (fmt(L4), fmt(L1))
            )

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = "\\True Lương bậc 5 của anh Bình sẽ là %s đồng" % (fmt(L5))
            th_da_1_s = "Lương bậc 5 của anh Bình sẽ là %s đồng" % (fmt(L5 - 1000000))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = (
                "Mức lương bậc 5 của anh Bình là: \\\\"
                "$L_5 = L_4 \\cdot 1,25 = %s \\cdot 1,25 = %s$ đồng."
                % (fmt(L4), fmt(L5))
            )

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = "\\True Lương bậc 7 của anh Bình là %s đồng" % (fmt(L7))
            vd_da_1_s = "Lương bậc 7 của anh Bình là %s đồng" % (fmt(L7 + 1000000))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = (
                "Mức lương bậc 7 của anh Bình là: \\\\"
                "$L_7 = L_1 \\cdot 1,25^6 = %s \\cdot 1,25^6 \\approx %s$ đồng."
                % (fmt(L1), fmt(L7))
            )

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = (
                "\\True Tổng tiền lương anh Bình nhận được kể từ khi hết tập sự đến khi nghỉ hưu là %s đồng"
                % (fmt(T_tong))
            )
            vdc_da_1_s = (
                "Tổng tiền lương anh Bình nhận được kể từ khi hết tập sự đến khi nghỉ hưu là %s đồng"
                % (fmt(T_tong + 200000000))
            )
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = (
                "Thời gian làm việc gồm 21 năm ở 7 bậc lương và %s năm vượt khung. \\\\"
                "+ Tổng tiền lương 21 năm đầu (bậc 1 đến bậc 7) gồm 7 giai đoạn, mỗi giai đoạn 36 tháng: \\\\"
                "$T_{21} = 36 \\cdot L_1 \\cdot \\frac{1,25^7 - 1}{1,25 - 1} \\approx %s$ đồng. \\\\"
                "+ Mức lương tháng đầu tiên của năm vượt khung thứ nhất là: $L_{VK1} = L_7 \\cdot 1,01 \\approx %s$ đồng. \\\\"
                "+ Tổng tiền lương trong %s năm vượt khung là: \\\\"
                "$T_{VK} = 12 \\cdot L_{VK1} \\cdot \\frac{1,01^{%s} - 1}{1,01 - 1} \\approx %s$ đồng. \\\\"
                "Vậy tổng tiền lương anh Bình nhận được trong %s năm là: \\\\"
                "$T = T_{21} + T_{VK} \\approx %s$ đồng."
                % (
                    nam_vuot_khung,
                    fmt(T21),
                    fmt(L_vk_1),
                    nam_vuot_khung,
                    nam_vuot_khung,
                    fmt(T_vk),
                    tong_nam,
                    fmt(T_tong),
                )
            )

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)


            def count_true_answers(answers):
                return sum("\\True" in ans for ans in answers)


            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n"
                + str(noidungcauhoi)
                + "\n\\choiceTFn \n"
                "{" + str(shuffled_answers_nb[0]) + "}\n"
                "{" + str(shuffled_answers_th[0]) + "}\n"
                "{" + str(shuffled_answers_vd[0]) + "}\n"
                "{" + str(shuffled_answers_vdc[0]) + "}\n"
                "\\loigiai{ \n"
                "\\begin{enumEX}[a)]{1} \n"
                "\\item " + str(shuffled_solutions_nb[0]) + "\n"
                "\\item " + str(shuffled_solutions_th[0]) + "\n"
                "\\item " + str(shuffled_solutions_vd[0]) + "\n"
                "\\item " + str(shuffled_solutions_vdc[0]) + "\n"
                "\\end{enumEX}} \n"
                "\\end{ex}\n \\end{minipage}\n\n")
            return content

