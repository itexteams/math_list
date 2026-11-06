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


def bt_dang16_p2_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến và tạo ngẫu nhiên thông số bài toán
            u1 = 1
            q = 2
            N = 64
            n_hat = 100
            m_hat = random.choice([15, 20, 25])  # Khối lượng của n_hat hạt thóc (gam)
            k_th = random.randint(7, 9)          # Ô thứ k_th trong câu hỏi TH
            k_tau = random.choice([30, 32, 34])   # Số ô chở bằng tàu thủy trong VDC
            cap_tau = random.choice([5, 10, 20]) # Sức chở tối đa của tàu thủy (tấn)

            # Tính toán các giá trị phục vụ đáp án và lời giải
            u_kth = u1 * (q ** (k_th - 1))

            # Tổng số hạt 64 ô
            S_N = u1 * (q ** N - 1) // (q - 1)
            m_1hat = m_hat / n_hat  # Khối lượng 1 hạt (gam)
            m_1hat_str = str(m_1hat).replace('.', ',')

            # Khối lượng 64 ô theo tỉ tấn (1 tỉ tấn = 10^15 gam)
            val_ti_tan = round(S_N * m_1hat / (10**15))
            val_ti_tan_sai = val_ti_tan - random.choice([20, 30, 40])

            # Khối lượng k_tau ô đầu tiên theo tấn (1 tấn = 10^6 gam)
            S_ktau = u1 * (q ** k_tau - 1) // (q - 1)
            W_ktau_tan = S_ktau * m_1hat / (10**6)
            W_ktau_tan_str = str(round(W_ktau_tan, 2)).replace('.', ',')
            N_trips = math.ceil(W_ktau_tan / cap_tau)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Tương truyền rằng nhà vua Ấn Độ cho phép người phát minh ra bàn cờ vua được lựa chọn phần thưởng tùy theo sở thích. Người đó xin nhà vua: "Bàn cờ có %s ô, với ô thứ nhất thần xin nhận %s hạt thóc, ô thứ hai thì gấp %s ô đầu, ô thứ ba thì lại gấp %s ô thứ hai, ... cứ như vậy ô sau nhận số hạt thóc gấp %s phần thưởng dành cho ô liền trước và thần xin nhận tổng số các hạt thóc ở %s ô". Biết rằng khối lượng của %s hạt thóc là %s gam.'''
                            %(N, u1, q, q, q, N, n_hat, m_hat))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Số hạt thóc ở %s ô là một cấp số nhân có $u_1=%s; q=%s$' %(N, u1, q)
            nb_da_1_s = 'Số hạt thóc ở %s ô là một cấp số cộng có $u_1=%s; d=%s$' %(N, u1, q)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Số hạt thóc ở mỗi ô (từ ô thứ nhất đến ô thứ %s) lập thành một cấp số nhân có số hạng đầu $u_1=%s$ và công bội $q=%s$.'''
                            %(N, u1, q))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Số hạt thóc ở ô thứ %s là $%s^{%s}$' %(k_th, q, k_th - 1)
            th_da_1_s = 'Số hạt thóc ở ô thứ %s là $%s^{%s}$' %(k_th, q, k_th)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Số hạt thóc ở ô thứ %s là $u_{%s} = u_1 \\cdot q^{%s} = %s \\cdot %s^{%s} = %s^{%s}$.'''
                            %(k_th, k_th, k_th - 1, u1, q, k_th - 1, q, k_th - 1))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Tổng khối lượng thóc của %s ô trên bàn cờ khoảng %s tỉ tấn' %(N, val_ti_tan)
            vd_da_1_s = 'Tổng khối lượng thóc của %s ô trên bàn cờ khoảng %s tỉ tấn' %(N, val_ti_tan_sai)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Tổng số hạt thóc ở %s ô là $S_{%s} = \\frac{u_1(q^{%s}-1)}{q-1} = %s^{%s}-1$ hạt. \\\\
            Khối lượng của $1$ hạt thóc là $\\frac{%s}{%s} = %s$ gam. \\\\
            Tổng khối lượng thóc trên bàn cờ là $(%s^{%s}-1) \\cdot %s$ gam $\\approx %s$ tỉ tấn.'''
                            %(N, N, N, q, N, m_hat, n_hat, m_1hat_str, q, N, m_1hat_str, val_ti_tan))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Giả sử người đó muốn chở số thóc ở trên %s ô đầu tiên về bằng tàu thủy, biết rằng mỗi chuyến tàu chở tối đa %s tấn hàng hóa. Khi đó, người đó cần tối thiểu %s chuyến tàu để chở hết số thóc đó' %(k_tau, cap_tau, N_trips)
            vdc_da_1_s = 'Giả sử người đó muốn chở số thóc ở trên %s ô đầu tiên về bằng tàu thủy, biết rằng mỗi chuyến tàu chở tối đa %s tấn hàng hóa. Khi đó, người đó cần tối thiểu %s chuyến tàu để chở hết số thóc đó' %(k_tau, cap_tau, N_trips - 1)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Tổng số hạt thóc ở %s ô đầu tiên là $S_{%s} = %s^{%s}-1$ hạt. \\\\
            Khối lượng của số thóc này là $(%s^{%s}-1) \\cdot %s$ gam $\\approx %s$ tấn. \\\\
            Số chuyến tàu tối thiểu cần dùng là $\\left\\lceil \\frac{%s}{%s} \\right\\rceil = %s$ chuyến.'''
                            %(k_tau, k_tau, q, k_tau, q, k_tau, m_1hat_str, W_ktau_tan_str, W_ktau_tan_str, cap_tau, N_trips))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

