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


def bt_dang19_p2_b1_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Random số liệu
            m_bo = random.choice([100, 150])
            calo_bo = random.choice([250, 300])
            m_trung = random.choice([44, 50])
            calo_trung = random.choice([70, 80])
            calo_max = random.choice([700, 800])

            rate_bo = str(round(float(calo_bo / m_bo), 1)).replace('.', ',') if float(calo_bo / m_bo) % 1 != 0 else str(int(calo_bo / m_bo))

            # Các giá trị để test tính đúng/sai
            test_x_b = random.choice([250, 280, 300]) # Khối lượng thịt bò max (thực tế) = calo_max / (calo_bo/m_bo)
            max_bo_real = float(calo_max) / (calo_bo / m_bo)
            is_b_true = test_x_b == int(max_bo_real)

            test_x_c = random.choice([250, 260])
            test_y_c = random.choice([2, 3])
            calo_c = test_x_c * float(calo_bo / m_bo) + test_y_c * calo_trung
            is_c_true = calo_c <= calo_max

            test_x_d = random.choice([200, 220])
            test_y_d = random.choice([2, 3])
            calo_d = test_x_d * float(calo_bo / m_bo) + test_y_d * calo_trung
            is_d_true = calo_d <= calo_max

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho biết mỗi $%s\\text{ g}$ thịt bò chứa $%s$ calo, một quả trứng nặng $%s\\text{ g}$ chứa $%s$ calo. Ông A đang có dấu hiệu bị bệnh cao huyết áp, nên bác sĩ dinh dưỡng của ông A yêu cầu ông mỗi buổi sáng không được hấp thụ quá $%s$ calo. Gọi số gam thịt bò và số quả trứng mà ông A ăn trong một buổi sáng lần lượt là $x$ và $y$.''' 
                             % (m_bo, calo_bo, m_trung, calo_trung, calo_max))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Bất phương trình : $%s x + %s y \\le %s$ biểu diễn giới hạn về lượng calo được hấp thụ của ông A mỗi sáng' % (rate_bo, calo_trung, calo_max)
            nb_da_1_s = 'Bất phương trình : $%s x + %s y \\ge %s$ biểu diễn giới hạn về lượng calo được hấp thụ của ông A mỗi sáng' % (rate_bo, calo_trung, calo_max)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Mỗi $%s\\text{ g}$ thịt bò có $%s$ calo, suy ra $1\\text{ g}$ thịt bò có $\\frac{%s}{%s} = %s$ calo. \\\\
            Mỗi quả trứng có $%s$ calo. \\\\
            Do đó, tổng lượng calo mà ông A hấp thụ khi ăn $x$ gam thịt bò và $y$ quả trứng là: $%s x + %s y$. \\\\
            Vì bác sĩ yêu cầu không vượt quá $%s$ calo nên ta có bất phương trình: $%s x + %s y \\le %s$.'''
                            % (m_bo, calo_bo, calo_bo, m_bo, rate_bo, calo_trung, rate_bo, calo_trung, calo_max, rate_bo, calo_trung, calo_max))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            if is_b_true:
                th_da_1_d = '\\True Nếu chỉ ăn thịt bò, thì ông A có thể ăn tối đa $%s\\text{ g}$ thịt bò vào mỗi sáng' % (test_x_b)
                th_da_1_s = 'Nếu chỉ ăn thịt bò, thì ông A có thể ăn tối đa $%s\\text{ g}$ thịt bò vào mỗi sáng' % (test_x_b + 50)
            else:
                th_da_1_d = '\\True Nếu chỉ ăn thịt bò, thì ông A có thể ăn tối đa $%s\\text{ g}$ thịt bò vào mỗi sáng' % (int(max_bo_real))
                th_da_1_s = 'Nếu chỉ ăn thịt bò, thì ông A có thể ăn tối đa $%s\\text{ g}$ thịt bò vào mỗi sáng' % (test_x_b)

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Nếu chỉ ăn thịt bò (tức là $y = 0$), ta thay vào bất phương trình $%s x + %s y \\le %s$: \\\\
            $%s x \\le %s \\Leftrightarrow x \\le %s$. \\\\
            Vậy ông A có thể ăn tối đa $%s\\text{ g}$ thịt bò.'''       
                            % (rate_bo, calo_trung, calo_max, rate_bo, calo_max, int(max_bo_real), int(max_bo_real)))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Các đáp án
            if is_c_true:
                vd_da_1_d = '\\True Ông A ăn $%s\\text{ g}$ thịt bò và $%s$ quả trứng vào buổi sáng là phù hợp yêu cầu của bác sĩ' % (test_x_c, test_y_c)
                vd_da_1_s = 'Ông A ăn $%s\\text{ g}$ thịt bò và $%s$ quả trứng vào buổi sáng là không phù hợp yêu cầu của bác sĩ' % (test_x_c, test_y_c)
            else:
                vd_da_1_d = '\\True Ông A ăn $%s\\text{ g}$ thịt bò và $%s$ quả trứng vào buổi sáng là không phù hợp yêu cầu của bác sĩ' % (test_x_c, test_y_c)
                vd_da_1_s = 'Ông A ăn $%s\\text{ g}$ thịt bò và $%s$ quả trứng vào buổi sáng là phù hợp yêu cầu của bác sĩ' % (test_x_c, test_y_c)

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            cmp_c = "\\le" if is_c_true else ">"
            res_c = "phù hợp" if is_c_true else "không phù hợp"
            str_calo_c = str(round(calo_c, 1)).replace('.', ',') if calo_c % 1 != 0 else str(int(calo_c))
            loigiai_vd_1 = ('''Thay $x = %s$ và $y = %s$ vào vế trái của bất phương trình, ta có lượng calo hấp thụ là: \\\\
            $%s \\cdot %s + %s \\cdot %s = %s$ (calo). \\\\
            Vì $%s %s %s$, nên khẩu phần ăn này %s với yêu cầu của bác sĩ.'''
                            % (test_x_c, test_y_c, rate_bo, test_x_c, calo_trung, test_y_c, str_calo_c, str_calo_c, cmp_c, calo_max, res_c))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Các đáp án
            if is_d_true:
                vdc_da_1_d = '\\True Ông A ăn $%s\\text{ g}$ thịt bò và $%s$ quả trứng vào buổi sáng là phù hợp yêu cầu của bác sĩ' % (test_x_d, test_y_d)
                vdc_da_1_s = 'Ông A ăn $%s\\text{ g}$ thịt bò và $%s$ quả trứng vào buổi sáng là không phù hợp yêu cầu của bác sĩ' % (test_x_d, test_y_d)
            else:
                vdc_da_1_d = '\\True Ông A ăn $%s\\text{ g}$ thịt bò và $%s$ quả trứng vào buổi sáng là không phù hợp yêu cầu của bác sĩ' % (test_x_d, test_y_d)
                vdc_da_1_s = 'Ông A ăn $%s\\text{ g}$ thịt bò và $%s$ quả trứng vào buổi sáng là phù hợp yêu cầu của bác sĩ' % (test_x_d, test_y_d)

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            cmp_d = "\\le" if is_d_true else ">"
            res_d = "phù hợp" if is_d_true else "không phù hợp"
            str_calo_d = str(round(calo_d, 1)).replace('.', ',') if calo_d % 1 != 0 else str(int(calo_d))
            loigiai_vdc_1 = ('''Thay $x = %s$ và $y = %s$ vào vế trái của bất phương trình, ta có lượng calo hấp thụ là: \\\\
            $%s \\cdot %s + %s \\cdot %s = %s$ (calo). \\\\
            Vì $%s %s %s$, nên khẩu phần ăn này %s với yêu cầu của bác sĩ.'''
                             % (test_x_d, test_y_d, rate_bo, test_x_d, calo_trung, test_y_d, str_calo_d, str_calo_d, cmp_d, calo_max, res_d))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

