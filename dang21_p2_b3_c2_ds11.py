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


def bt_dang21_p2_b3_c2_ds11(self):
            # Khai báo biến
            # --- B3: KHAI BÁO VÀ NGẪU NHIÊN HÓA CÁC THAM SỐ ---
            u1 = random.choice([80, 100, 120, 150])  # Mức lương năm đầu (triệu)
            d = random.choice([10, 15, 20, 25])  # Mức tăng mỗi năm (triệu)

            # Chi tiêu hàng năm (đảm bảo nhỏ hơn u1)
            chi_tieu = random.choice([50, 60, 70, 80])
            while chi_tieu >= u1:
                chi_tieu -= 10

            # Giá trị căn chung cư (tỉ đồng)
            T_ti = random.choice([1.5, 2.0, 2.5, 3.0])
            T_trieu = int(T_ti * 1000)
            T_ti_str = (
                str(T_ti).replace(".", ",")
                if isinstance(T_ti, float) and T_ti % 1 != 0
                else str(int(T_ti))
            )

            # Tính toán các giá trị
            u2 = u1 + d
            u10 = u1 + 9 * d

            # Dãy tiết kiệm v_n = u_n - chi_tieu
            v1 = u1 - chi_tieu
            # S_n = n/2 * [2*v1 + (n-1)*d] >= T_trieu
            # <=> d * n^2 + (2*v1 - d) * n - 2*T_trieu >= 0
            A_eq = d
            B_eq = 2 * v1 - d
            C_eq = 2 * T_trieu

            delta = B_eq**2 + 4 * A_eq * C_eq
            n_exact = (-B_eq + math.sqrt(delta)) / (2 * A_eq)
            N_min = math.ceil(n_exact)

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (
                "Một sinh viên sau khi ra trường và xin vào làm cho một trung tâm với mức lương khởi điểm là %s triệu đồng một năm. "
                "Cứ sau mỗi năm, trung tâm trả thêm cho sinh viên %s triệu đồng. Gọi $u_n$ là số tiền lương mà sinh viên đó nhận được ở năm thứ $n$. "
                "Hỏi các mệnh đề sau đúng hay sai?" % (u1, d)
            )

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = (
                "\\True Số tiền lương sinh viên nhận được ở năm thứ hai là %s triệu đồng"
                % (u2)
            )
            nb_da_1_s = (
                "Số tiền lương sinh viên nhận được ở năm thứ hai là %s triệu đồng"
                % (u2 + 10)
            )
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = (
                "Số tiền lương sinh viên nhận được ở năm thứ hai là: \\\\"
                "$u_2 = u_1 + d = %s + %s = %s$ triệu đồng." % (u1, d, u2)
            )
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = (
                "\\True Số tiền lương sinh viên nhận được ở năm thứ 10 là %s triệu đồng"
                % (u10)
            )
            th_da_1_s = (
                "Số tiền lương sinh viên nhận được ở năm thứ 10 là %s triệu đồng"
                % (u10 + 20)
            )
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = (
                "Số tiền lương sinh viên nhận được ở năm thứ 10 là: \\\\"
                "$u_{10} = u_1 + 9d = %s + 9 \\cdot %s = %s$ triệu đồng." % (u1, d, u10)
            )
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = (
                "\\True Dãy số $(u_n)$ là cấp số cộng có $u_1 = %s$ và công sai $d = %s$"
                % (u1, d)
            )
            vd_da_1_s = (
                "Dãy số $(u_n)$ là cấp số cộng có $u_1 = %s$ và công sai $d = %s$"
                % (u2, d)
            )
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = (
                "Vì mỗi năm tiền lương tăng thêm %s triệu đồng nên dãy số $(u_n)$ là một cấp số cộng với số hạng đầu $u_1 = %s$ và công sai $d = %s$."
                % (d, u1, d)
            )
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = (
                "\\True Giả sử, mỗi năm bạn sinh viên chi tiêu tiết kiệm hết %s triệu đồng. Vậy sau ít nhất %s năm thì sinh viên đó mua được căn chung cư %s tỉ đồng"
                % (chi_tieu, N_min, T_ti_str)
            )
            vdc_da_1_s = (
                "Giả sử, mỗi năm bạn sinh viên chi tiêu tiết kiệm hết %s triệu đồng. Vậy sau ít nhất %s năm thì sinh viên đó mua được căn chung cư %s tỉ đồng"
                % (chi_tieu, N_min - 2, T_ti_str)
            )
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = (
                "Số tiền sinh viên tiết kiệm được ở năm thứ $n$ là: $v_n = u_n - %s$ triệu đồng. \\\\"
                "Dãy số $(v_n)$ lập thành một cấp số cộng với số hạng đầu $v_1 = %s - %s = %s$ triệu đồng và công sai $d = %s$. \\\\"
                "Tổng số tiền tiết kiệm được sau $n$ năm là: \\\\"
                "$S_n = \\frac{n}{2} \\cdot \\left[ 2v_1 + (n - 1)d \\right] = \\frac{n}{2} \\cdot \\left[ 2 \\cdot %s + (n - 1) \\cdot %s \\right]$ triệu đồng. \\\\"
                "Đổi %s tỉ đồng = %s triệu đồng. \\\\"
                "Để đủ tiền mua chung cư thì $S_n \\ge %s \\Leftrightarrow %s n^2 + %s n - %s \\ge 0 \\Rightarrow n \\ge %s$. \\\\"
                "Vì $n \\in \\mathbb{N}^*$ nên sau ít nhất %s năm thì sinh viên đó mua được căn chung cư."
                % (
                    chi_tieu,
                    u1,
                    chi_tieu,
                    v1,
                    d,
                    v1,
                    d,
                    T_ti_str,
                    T_trieu,
                    T_trieu,
                    A_eq,
                    B_eq,
                    C_eq,
                    round(n_exact, 2),
                    N_min,
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

