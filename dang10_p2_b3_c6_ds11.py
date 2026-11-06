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


def bt_dang10_p2_b3_c6_ds11(self):
            # Khai báo biến
            # p là xác suất một bóng đèn bị hỏng
            list_p = [0.1, 0.12, 0.15, 0.18, 0.2]
            p = random.choice(list_p)
            q = 1 - p

            # Các giá trị tính toán
            p_fail_II = round(p**2, 4) # Hệ thống II hỏng (song song)
            p_work_II = round(1 - p_fail_II, 4) # Hệ thống II hoạt động
            p_fail_I = round(1 - q**2, 4) # Hệ thống I hỏng (nối tiếp)
            p_both_fail = round(p_fail_I * p_fail_II, 5) # Cả hai hệ thống hỏng

            # Chuyển đổi dấu chấm thành dấu phẩy cho hiển thị tiếng Việt
            def v(num):
                return str(num).replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trên một bảng quảng cáo, người ta mắc hai hệ thống bóng đèn. Hệ thống $I$ gồm $2$ bóng mắc nối tiếp, hệ thống $II$ gồm $2$ bóng mắc song song. Khả năng bị hỏng của mỗi bóng đèn sau $6$ giờ thắp sáng liên tục là $%s$. Biết tình trạng của mỗi bóng đèn là độc lập.''' 
                             % (v(p)))

            ########################################################################
            # Nhận biết - Hệ thống II bị hỏng
            ########################################################################
            nb_da_1_d = '\\True Hệ thống $II$ bị hỏng (không sáng) bằng $%s$' % (v(p_fail_II))
            nb_da_1_s = 'Hệ thống $II$ bị hỏng (không sáng) bằng $%s$' % (v(round(p_fail_II + 0.01, 4)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Hệ thống $II$ gồm $2$ bóng mắc song song nên hệ thống hỏng khi cả $2$ bóng cùng hỏng. \\\\ Xác suất là $P_{II} = %s \\cdot %s = %s$.''' 
                            % (v(p), v(p), v(p_fail_II)))

            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu - Hệ thống II hoạt động bình thường
            ########################################################################
            th_da_1_d = '\\True Xác suất để hệ thống $II$ hoạt động bình thường bằng $%s$' % (v(p_work_II))
            th_da_1_s = 'Xác suất để hệ thống $II$ hoạt động bình thường bằng $%s$' % (v(round(p_work_II - 0.02, 4)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Hệ thống $II$ hoạt động bình thường là biến cố đối của biến cố hệ thống $II$ bị hỏng. \\\\ Xác suất là $1 - P_{II} = 1 - %s = %s$.''' 
                            % (v(p_fail_II), v(p_work_II)))

            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng - Hệ thống I bị hỏng
            ########################################################################
            vd_da_1_d = '\\True Hệ thống $I$ bị hỏng (không sáng) bằng $%s$' % (v(p_fail_I))
            vd_da_1_s = 'Hệ thống $I$ bị hỏng (không sáng) bằng $%s$' % (v(round(p_fail_I + 0.3, 4)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Hệ thống $I$ gồm $2$ bóng mắc nối tiếp nên hệ thống hỏng khi có ít nhất một bóng hỏng. \\\\ Xác suất hệ thống $I$ hoạt động (cả $2$ bóng đều tốt) là $(1-%s)^2 = %s^2 = %s$. \\\\ Vậy xác suất hệ thống $I$ hỏng là $1 - %s = %s$.''' 
                            % (v(p), v(q), v(round(q**2, 4)), v(round(q**2, 4)), v(p_fail_I)))

            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao - Cả hai hệ thống bị hỏng
            ########################################################################
            vdc_da_1_d = '\\True Cả hai hệ thống bị hỏng (kết quả được làm tròn đến hàng phần trăm nghìn) bằng $%s$' % (v(p_both_fail))
            vdc_da_1_s = 'Cả hai hệ thống bị hỏng (kết quả được làm tròn đến hàng phần trăm nghìn) bằng $%s$' % (v(round(p_both_fail + 0.02, 5)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Vì hai hệ thống hoạt động độc lập nên xác suất cả hai hệ thống cùng hỏng là tích các xác suất hỏng của từng hệ thống: \\\\ $P = P_{I} \\cdot P_{II} = %s \\cdot %s = %s$.''' 
                             % (v(p_fail_I), v(p_fail_II), v(p_both_fail)))

            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi có từ 1 đến 3 đáp án đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán vào list xáo trộn theo logic mẫu
            combined_nb = list(zip([nb_da_1], list_nb_2))
            combined_th = list(zip([th_da_1], list_th_2))
            combined_vd = list(zip([vd_da_1], list_vd_2))
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

