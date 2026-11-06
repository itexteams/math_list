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


def bt_dang24_p2_b3_c2_ds11(self):
            # Khai báo biến
            # --- B3: KHAI BÁO VÀ NGẪU NHIÊN HÓA CÁC THAM SỐ ---
            tien_gui_nghin = random.choice([500, 600, 700, 800, 1000])  # Nghìn đồng
            tien_gui_trieu = tien_gui_nghin / 1000.0  # Triệu đồng

            lai_suat_pct = random.choice([0.4, 0.5, 0.6, 0.7])  # % / tháng
            r = lai_suat_pct / 100.0

            tuoi_bd = random.choice([2, 3, 4, 5])
            tuoi_kt = random.choice([18, 20])

            so_nam = tuoi_kt - tuoi_bd
            so_thang = so_nam * 12

            # Chuyển đổi dấu chấm thành dấu phẩy cho hiển thị tiếng Việt
            def to_str_vn(val):
                if isinstance(val, float):
                    if val.is_integer():
                        return str(int(val))
                    return str(round(val, 2)).replace(".", ",")
                return str(val)

            tien_gui_trieu_str = to_str_vn(tien_gui_trieu)
            lai_suat_pct_str = to_str_vn(lai_suat_pct)

            # Tính toán giá trị toán học
            # Sau 5 tháng (sau khi gửi khoản thứ 5)
            S_5_dong = (tien_gui_nghin * 1000 * (1 + r) / r) * ((1 + r)**5 - 1)
            S_5_str = "{:,}".format(int(round(S_5_dong))).replace(",", ".")

            # Tổng số tiền sau so_thang
            S_n_trieu = (tien_gui_trieu * (1 + r) / r) * ((1 + r)**so_thang - 1)
            S_n_trieu_rounded = round(S_n_trieu, 2)
            S_n_trieu_str = to_str_vn(S_n_trieu_rounded)

            # Mức so sánh cho câu d
            moc_so_sanh = int(round(S_n_trieu - 15))

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (
                "Để tích lũy cho việc học đại học của cậu con trai đầu lòng, cô Lan quyết định hằng tháng bỏ ra $%s$ "
                "nghìn đồng vào tài khoản tiết kiệm, được trả lãi $%s$\\%% cộng dồn hằng tháng. Cô bắt đầu chương "
                "trình tích lũy này khi cậu con trai tròn $%s$ tuổi và gửi tiền vào đầu mỗi tháng. "
                "Hỏi các mệnh đề sau đúng hay sai?" % (tien_gui_nghin, lai_suat_pct_str, tuoi_bd)
            )

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = (
                "\\True Đến lần gửi khoản tiền thứ $%s$ thì cậu con trai tròn $%s$ tuổi"
                % (so_thang, tuoi_kt)
            )
            nb_da_1_s = (
                "Đến lần gửi khoản tiền thứ $%s$ thì cậu con trai tròn $%s$ tuổi"
                % (so_thang + 12, tuoi_kt)
            )
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = (
                "Thời gian từ khi con $%s$ tuổi đến khi tròn $%s$ tuổi là $%s$ năm, tương ứng với $%s \\cdot 12 = %s$ tháng. \\\\"
                "Do gửi tiền vào đầu mỗi tháng nên đến lần gửi thứ $%s$ thì cậu con trai tròn $%s$ tuổi."
                % (tuoi_bd, tuoi_kt, so_nam, so_nam, so_thang, so_thang, tuoi_kt)
            )
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = (
                "\\True Số tiền của cô Lan có trong chương trình ở đầu tháng thứ 2 (trước khi gửi khoản thứ hai) là $%s(1 + %s\\%%)$ triệu đồng"
                % (tien_gui_trieu_str, lai_suat_pct_str)
            )
            th_da_1_s = (
                "Số tiền của cô Lan có trong chương trình ở đầu tháng thứ 2 (trước khi gửi khoản thứ hai) là $%s(1 + %s\\%%)$ triệu đồng"
                % (tien_gui_trieu_str, to_str_vn(lai_suat_pct * 2))
            )
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = (
                "Ở đầu tháng thứ 1, cô Lan gửi vào $%s$ triệu đồng. \\\\"
                "Đến đầu tháng thứ 2, khoản tiền này đã sinh lãi trong 1 tháng nên số tiền tích lũy thu được là $%s \\cdot (1 + %s\\%%)$ triệu đồng."
                % (tien_gui_trieu_str, tien_gui_trieu_str, lai_suat_pct_str)
            )
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = (
                "\\True Số tiền của cô Lan có trong chương trình ở đầu tháng thứ 5 (sau khi gửi khoản thứ 5) xấp xỉ $%s$ đồng"
                % (S_5_str)
            )
            vd_da_1_s = (
                "Số tiền của cô Lan có trong chương trình ở đầu tháng thứ 5 (sau khi gửi khoản thứ 5) xấp xỉ $%s$ đồng"
                % ("{:,}".format(tien_gui_nghin * 5000 + 30000).replace(",", "."))
            )
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = (
                "Công thức tổng số tiền tích lũy sau $n$ tháng (ngay sau khi gửi khoản tiền thứ $n$) là: \\\\"
                "$S_n = \\frac{a(1+r)}{r} \\cdot \\left[ (1+r)^n - 1 \\right]$. \\\\"
                "Ở đầu tháng thứ 5, sau khi gửi khoản thứ 5, số tiền là: \\\\"
                "$S_5 = \\frac{%s \\cdot (1 + %s\\%%)}{%s\\%%} \\cdot \\left[ (1 + %s\\%%)^5 - 1 \\right] \\approx %s$ đồng."
                % (
                    "{:,}".format(tien_gui_nghin * 1000).replace(",", "."),
                    lai_suat_pct_str,
                    lai_suat_pct_str,
                    lai_suat_pct_str,
                    S_5_str,
                )
            )
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = (
                "\\True Số tiền của cô Lan có trong chương trình vào thời điểm cậu con trai đầu lòng tròn $%s$ tuổi lớn hơn $%s$ triệu đồng"
                % (tuoi_kt, moc_so_sanh)
            )
            vdc_da_1_s = (
                "Số tiền của cô Lan có trong chương trình vào thời điểm cậu con trai đầu lòng tròn $%s$ tuổi nhỏ hơn $%s$ triệu đồng"
                % (tuoi_kt, moc_so_sanh)
            )
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = (
                "Thời điểm con tròn $%s$ tuổi ứng với $n = %s$ tháng. \\\\"
                "Số tiền cô Lan nhận được là: \\\\"
                "$S_{%s} = \\frac{%s \\cdot (1 + %s\\%%)}{%s\\%%} \\cdot \\left[ (1 + %s\\%%)^{%s} - 1 \\right] \\approx %s$ triệu đồng. \\\\"
                "Do đó, số tiền thu được lớn hơn $%s$ triệu đồng."
                % (
                    tuoi_kt,
                    so_thang,
                    so_thang,
                    tien_gui_trieu_str,
                    lai_suat_pct_str,
                    lai_suat_pct_str,
                    lai_suat_pct_str,
                    so_thang,
                    S_n_trieu_str,
                    moc_so_sanh,
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
                "\\end{ex}\n \\end{minipage}\n\n" )
            return content

