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


def bt_dang17_p2_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo các tham số ngẫu nhiên cho bài toán
            t1 = random.randint(4, 5)  # Tuổi bắt đầu gửi tiết kiệm
            t2 = 18  # Tuổi kết thúc (đại học)
            n_total = t2 - t1  # Tổng số năm gửi ban đầu

            r_pct = random.choice([4.2, 4.5, 4.8, 5.0, 5.2, 5.5])  # Lãi suất %/năm
            r = r_pct / 100.0
            r_str = str(r_pct).replace(".", ",")

            S1 = random.choice([200, 220, 250, 300])  # Số tiền mục tiêu ban đầu (triệu)

            # Tính giá trị x nhỏ nhất (số nguyên)
            coef_x = (1 + r) * (((1 + r) ** n_total) - 1) / r
            x_val_exact = S1 / coef_x
            x_val = math.ceil(x_val_exact)
            x_exact_str = str(round(x_val_exact, 2)).replace(".", ",")

            # Các tham số cho phần Vận dụng cao
            t3 = random.randint(9, 11)  # Tuổi con gái khi dự định mua xe
            n1 = t3 - t1  # Số lần gửi x triệu
            n2 = t2 - t3  # Số lần gửi y triệu
            S_xe = random.choice([40, 50, 60])  # Giá trị xe máy (triệu)
            S2 = S1 + S_xe

            # Tính số tiền x tích lũy đến năm t2 tuổi
            Ax = x_val * ((1 + r) ** n2) * (1 + r) * (((1 + r) ** n1) - 1) / r
            Ax_str = str(round(Ax, 2)).replace(".", ",")

            # Hệ số tích lũy của y từ năm t3 đến t2
            coef_y = (1 + r) * (((1 + r) ** n2) - 1) / r
            coef_y_str = str(round(coef_y, 2)).replace(".", ",")

            # Tính giá trị y nhỏ nhất (số nguyên)
            y_val_exact = (S2 - Ax) / coef_y
            y_val = math.ceil(y_val_exact)
            y_exact_str = str(round(y_val_exact, 2)).replace(".", ",")

            # Nội dung câu hỏi
            noidungcauhoi = (
                "Vào năm con gái được %s tuổi, một người chuẩn bị gửi tiết kiệm đầu mỗi năm một số tiền $x$ ($x \\in \\mathbb{N}$) "
                "để đến năm %s tuổi sẽ có được %s triệu cho con gái đi học đại học. Hiện tại lãi suất tiền gửi hàng năm là %s\\%%/năm. "
                "Giả sử lãi suất này được giữ ổn định." % (t1, t2, S1, r_str)
            )

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = (
                "\\True Tổng số tiền thu về sau %s năm là một cấp số nhân có công bội $q = 1 + %s\\%%$"
                % (n_total, r_str)
            )
            nb_da_1_s = (
                "Tổng số tiền thu về sau %s năm là một cấp số nhân có công bội $q = %s\\%%$"
                % (n_total, r_str)
            )
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = (
                "Các khoản tiền gửi đầu mỗi năm tích lũy theo thời gian tạo thành các số hạng của một cấp số nhân "
                "với công bội $q = 1 + r = 1 + %s\\%%$." % (r_str)
            )
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = (
                "\\True Cấp số nhân biểu diễn tổng số tiền thu về sau %s năm có số hạng đầu $u_1 = x(1 + %s\\%%)$"
                % (n_total, r_str)
            )
            th_da_1_s = (
                "Cấp số nhân biểu diễn tổng số tiền thu về sau %s năm có số hạng đầu $u_1 = x$"
                % (n_total)
            )
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = (
                "Khoản tiền $x$ gửi ở đầu năm thứ nhất, sau %s năm sẽ tích lũy thành $u_1 = x(1 + %s\\%%)^{%s}$, "
                "và khoản $x$ gửi ở năm cuối cùng (đầu năm thứ %s) tính đến cuối năm thứ %s sẽ thu được $x(1 + %s\\%%)$. "
                "Do đó số hạng đầu tiên của cấp số nhân (ứng với khoản gửi gần nhất) là $u_1 = x(1 + %s\\%%)$."
                % (n_total, r_str, n_total, n_total, n_total, r_str, r_str)
            )
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = "\\True Giá trị nhỏ nhất của $x$ là %s" % (x_val)
            vd_da_1_s = "\\True Giá trị nhỏ nhất của $x$ là %s" % (x_val - 1)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = (
                "Tổng số tiền thu được sau %s năm gửi tiết kiệm là tổng của %s số hạng đầu trong cấp số nhân: \\\\"
                "$S_{%s} = u_1 \\cdot \\frac{q^{%s} - 1}{q - 1} = x(1 + %s\\%%) \\cdot \\frac{(1 + %s\\%%)^{%s} - 1}{%s\\%%}$. \\\\"
                "Để có đủ %s triệu đồng thì $S_{%s} \\ge %s \\iff x \\cdot %s \\ge %s \\iff x \\ge %s$. \\\\"
                "Vì $x \\in \\mathbb{N}$ nên giá trị nhỏ nhất của $x$ là %s."
                % (
                    n_total,
                    n_total,
                    n_total,
                    n_total,
                    r_str,
                    r_str,
                    n_total,
                    r_str,
                    S1,
                    n_total,
                    S1,
                    str(round(coef_x, 4)).replace(".", ","),
                    S1,
                    x_exact_str,
                    x_val,
                )
            )
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = (
                "\\True Đến năm con gái được %s tuổi, người này dự định khi con gái được %s tuổi sẽ mua thêm cho con gái một chiếc xe máy trị giá %s triệu đồng. Do đó, kể từ thời điểm đầu năm con gái được %s tuổi người này cần gửi tiết kiệm $y$ triệu đồng ($y \\in \\mathbb{N}$) đến khi con gái %s tuổi. Giá trị nhỏ nhất của $y$ là %s"
                % (t3, t2, S_xe, t3, t2, y_val)
            )
            vdc_da_1_s = (
                "Đến năm con gái được %s tuổi, người này dự định khi con gái được %s tuổi sẽ mua thêm cho con gái một chiếc xe máy trị giá %s triệu đồng. Do đó, kể từ thời điểm đầu năm con gái được %s tuổi người này cần gửi tiết kiệm $y$ triệu đồng ($y \\in \\mathbb{N}$) đến khi con gái %s tuổi. Giá trị nhỏ nhất của $y$ là %s"
                % (t3, t2, S_xe, t3, t2, y_val - 2)
            )
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = (
                "Số tiền $x = %s$ triệu đã gửi trong %s năm đầu (từ đầu năm %s tuổi đến đầu năm %s tuổi, gồm %s lần gửi), "
                "khi tính đến năm %s tuổi sẽ tích lũy được: \\\\"
                "$A_x = %s \\cdot (1 + %s\\%%)^{%s} \\cdot (1 + %s\\%%) \\cdot \\frac{(1 + %s\\%%)^{%s} - 1}{%s\\%%} \\approx %s$ triệu đồng. \\\\"
                "Từ đầu năm %s tuổi đến đầu năm %s tuổi (gồm %s lần gửi $y$ triệu đồng), số tiền tích lũy từ khoản $y$ đến năm %s tuổi là: \\\\"
                "$A_y = y(1 + %s\\%%) \\cdot \\frac{(1 + %s\\%%)^{%s} - 1}{%s\\%%} \\approx %s y$ triệu đồng. \\\\"
                "Tổng số tiền người đó cần có khi con gái %s tuổi là %s + %s = %s triệu đồng. \\\\"
                "Ta có điều kiện: $A_x + A_y \\ge %s \\iff %s + %s y \\ge %s \\iff y \\ge %s$. \\\\"
                "Vì $y \\in \\mathbb{N}$ nên giá trị nhỏ nhất của $y$ là %s."
                % (
                    x_val,
                    n1,
                    t1,
                    t3 - 1,
                    n1,
                    t2,
                    x_val,
                    r_str,
                    n2,
                    r_str,
                    r_str,
                    n1,
                    r_str,
                    Ax_str,
                    t3,
                    t2 - 1,
                    n2,
                    t2,
                    r_str,
                    r_str,
                    n2,
                    r_str,
                    coef_y_str,
                    t2,
                    S1,
                    S_xe,
                    S2,
                    S2,
                    Ax_str,
                    coef_y_str,
                    S2,
                    y_exact_str,
                    y_val,
                )
            )
            list_vdc_2 = [loigiai_vdc_1]


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

