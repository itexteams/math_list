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


def bt_dang48_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Hàm định dạng số: đổi dấu chấm thành dấu phẩy và bỏ số thập phân nếu là số nguyên
            def fmt(val):
                if isinstance(val, float):
                    if val.is_integer():
                        return str(int(val))
                    return str(round(val, 4)).replace('.', ',')
                return str(val).replace('.', ',')

            # Random bộ dữ liệu để bài toán luôn có số liệu đẹp
            valid_data = []
            for NB in [60, 70, 75, 80]:
                for pAB_percent in [70, 75, 80, 85, 90]:
                    if (NB * pAB_percent) % 100 == 0:
                        nAB_val = (NB * pAB_percent) // 100
                        NnotB = 100 - NB
                        for pAnotB_percent in [10, 15, 20, 25, 30]:
                            if (NnotB * pAnotB_percent) % 100 == 0:
                                nAnotB_val = (NnotB * pAnotB_percent) // 100
                                valid_data.append({
                                    'NB': NB,
                                    'pAB': pAB_percent,
                                    'NnotB': NnotB,
                                    'pAnotB': pAnotB_percent,
                                    'nAB': nAB_val,
                                    'nAnotB': nAnotB_val
                                })

            data = random.choice(valid_data)
            NB = data['NB']
            NnotB = data['NnotB']
            pAB = data['pAB']
            pAnotB = data['pAnotB']
            nAB = data['nAB']
            nAnotB = data['nAnotB']

            n_notA_B = NB - nAB
            n_notA_notB = NnotB - nAnotB
            nA = nAB + nAnotB

            P_B = NB / 100.0
            P_notB = NnotB / 100.0
            P_A_given_B = pAB / 100.0
            P_A_given_notB = pAnotB / 100.0
            P_A = nA / 100.0

            # Dữ liệu cho câu d
            M_list = [20, 25, 30, 40, 50]
            M = random.choice(M_list)
            valid_K = [k for k in range(1, M) if ((M - k) * 100) % M == 0]
            K = random.choice(valid_K)
            pct_d = ((M - K) * 100) // M

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trước khi diễn ra trận Derby thành Manchester giữa MU-MC. Người ta phỏng vấn ngẫu nhiên 100 người hâm mộ của MU (có %s người đang mặc áo của đội bóng) về việc có nên xem trận đấu đó hay không. Kết quả cho thấy rằng %s người trả lời sẽ xem, %s người trả lời sẽ không xem. Nhưng thực tế cho thấy rằng tỉ lệ người hâm mộ MU thực sự xem trận đấu tương ứng với những cách trả lời “có xem” và “không xem” là %s\\%% và %s\\%%. Gọi $A$ là biến cố “Người được phỏng vấn thực sự sẽ xem trận đấu” và $B$ là biến cố “Người được phỏng vấn trả lời sẽ xem trận đấu”.''' 
                             % (M, NB, NnotB, pAB, pAnotB))

            ######################################################################## Nhận biết ############################################
            P_AB_val = nAB / 100.0
            P_AB_wrong = round(P_AB_val + 0.1, 2)

            nb_da_1_d = '\\True $P(AB) = %s$' % (fmt(P_AB_val))
            nb_da_1_s = '$P(AB) = %s$' % (fmt(P_AB_wrong))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''\\begin{center}
            \\begin{tabular}{|c|c|c|}
            \\hline
            \\backslashbox{\\textbf{Phỏng vấn}}{\\textbf{Thực tế}} & \\textbf{Người xem thật} & \\textbf{Người không xem thật} \\\\
            \\hline
            Người trả lời sẽ xem (%s) & $%s \\cdot %s = %s$ & $%s - %s = %s$ \\\\
            \\hline
            Người trả lời sẽ không xem (%s) & $%s \\cdot %s = %s$ & $%s - %s = %s$ \\\\
            \\hline
            \\end{tabular}
            \\end{center}
            $AB$ là tập hợp người được phỏng vấn trả lời sẽ xem và xem thật nên do đó $n(AB) = %s$. \\\\
            Vậy $P(AB) = \\frac{%s}{100} = %s$ nên \\textbf{mệnh đề a) %s}''' % (
                NB, fmt(P_A_given_B), NB, nAB, NB, nAB, n_notA_B,
                NnotB, fmt(P_A_given_notB), NnotB, nAnotB, NnotB, nAnotB, n_notA_notB,
                nAB, nAB, fmt(P_AB_val), "{mda}"
            ))
            list_nb_2 = [loigiai_nb_1]

            ######################################################################## Thông hiểu ############################################
            pct_A_val = nA
            pct_A_wrong = nA + random.choice([-5, 5, 10])

            th_da_1_d = '\\True Tỉ lệ người được phỏng vấn thực sự sẽ xem trận đấu là %s\\%%' % (fmt(pct_A_val))
            th_da_1_s = 'Tỉ lệ người được phỏng vấn thực sự sẽ xem trận đấu là %s\\%%' % (fmt(pct_A_wrong))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''$A$ là tập hợp người được phỏng vấn xem thật trận đấu nên $n(A) = %s + %s = %s$. \\\\
            Do đó $P(A) = \\frac{%s}{100} = %s$ suy ra tỉ lệ người được phỏng vấn thực sự sẽ xem trận đấu là %s\\%% nên \\textbf{mệnh đề b) %s}''' % (
                nAB, nAnotB, nA, nA, fmt(P_A), fmt(pct_A_val), "{mdb}"
            ))
            list_th_2 = [loigiai_th_1]

            ######################################################################## Vận dụng ############################################
            val_c_exact = (nAnotB / nA) * 100
            val_c_approx = round(val_c_exact, 2)
            val_c_wrong = random.choice([15, 17, 20, 25, 30])
            while abs(val_c_wrong - val_c_approx) < 1:
                val_c_wrong = random.choice([15, 17, 20, 25, 30])

            if val_c_exact.is_integer():
                c_ratio_str = "= %s\\%%" % fmt(val_c_exact)
                c_ans_d_str = "%s" % fmt(val_c_exact)
            else:
                c_ratio_str = "\\approx %s\\%%" % fmt(val_c_approx)
                c_ans_d_str = "%s" % fmt(val_c_approx)

            vd_da_1_d = '\\True Trong số người được phỏng vấn thực sự sẽ xem có %s\\%% người trả lời không xem khi được phỏng vấn' % (c_ans_d_str)
            vd_da_1_s = 'Trong số người được phỏng vấn thực sự sẽ xem có %s\\%% người trả lời không xem khi được phỏng vấn' % (fmt(val_c_wrong))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Ngoài ra, ta có thể thực hiện tìm $P(A)$ theo công thức xác suất toàn phần như sau: \\\\
            Theo bài ra ta có: $P(B) = %s$; $P(\\overline{B}) = %s$; $P(A|B) = %s$; $P(A|\\overline{B}) = %s$. \\\\
            Do đó, $P(A) = P(B) \\cdot P(A|B) + P(\\overline{B}) \\cdot P(A|\\overline{B}) = %s \\cdot %s + %s \\cdot %s = %s$. \\\\
            Tổng số người được phỏng vấn thực sự sẽ xem thật trận đấu là $%s$ người. \\\\
            Số người trả lời không xem khi được phỏng vấn là $%s$ người. \\\\
            Tỉ lệ người trả lời không xem khi được phỏng vấn trong số những người thực sự xem trận đấu là $\\frac{%s}{%s} %s$ nên \\textbf{mệnh đề c) %s}''' % (
                fmt(P_B), fmt(P_notB), fmt(P_A_given_B), fmt(P_A_given_notB),
                fmt(P_B), fmt(P_A_given_B), fmt(P_notB), fmt(P_A_given_notB), fmt(P_A),
                nA, nAnotB, nAnotB, nA, c_ratio_str, "{mdc}"
            ))
            list_vd_2 = [loigiai_vd_1]

            ######################################################################## Vận dụng cao ############################################
            pct_d_wrong = pct_d + random.choice([5, 10, -5, -10])
            if pct_d_wrong <= 0: pct_d_wrong += 20

            vdc_da_1_d = '\\True Trong số những người mặc áo đội bóng có %s\\%% người phỏng vấn thực sự sẽ không xem trận đấu biết rằng số người được phỏng vấn thực sự sẽ xem trận đấu mặc áo đội bóng là %s người' % (pct_d, K)
            vdc_da_1_s = 'Trong số những người mặc áo đội bóng có %s\\%% người phỏng vấn thực sự sẽ không xem trận đấu biết rằng số người được phỏng vấn thực sự sẽ xem trận đấu mặc áo đội bóng là %s người' % (pct_d_wrong, K)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Tỉ lệ người phỏng vấn thực sự sẽ không xem trận đấu trong số những người mặc áo đội bóng là $\\frac{%s - %s}{%s} = %s\\%%$ nên \\textbf{mệnh đề d) %s}''' % (
                M, K, M, pct_d, "{mdd}"
            ))
            list_vdc_2 = [loigiai_vdc_1]


            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

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

            # Dùng hàm .replace() thay vì .format() để tránh lỗi với cặp ngoặc nhọn của LaTeX
            loigiai_nb_1 = loigiai_nb_1.replace("{mda}", "đúng" if "\\True" in nb_da_1 else "sai")
            loigiai_th_1 = loigiai_th_1.replace("{mdb}", "đúng" if "\\True" in th_da_1 else "sai")
            loigiai_vd_1 = loigiai_vd_1.replace("{mdc}", "đúng" if "\\True" in vd_da_1 else "sai")
            loigiai_vdc_1 = loigiai_vdc_1.replace("{mdd}", "đúng" if "\\True" in vdc_da_1 else "sai")

            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

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
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content

