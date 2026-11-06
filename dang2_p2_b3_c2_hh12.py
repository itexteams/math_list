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


def bt_dang2_p2_b3_c2_hh12(self):
            # Khai báo biến
            x,y,z,t=symbols('x,y,z,t')
            a1=randint(-6,6)
            b1=randint(-6,6)
            c1=randint(-7,7)
            d1=randint(-15,15)
            a2=randint(-6,6)
            b2=randint(-6,6)
            c2=randint(-7,7)
            d2=randint(-15,15)
            xa=randint(-6,6)
            ya=randint(-6,6)
            za=randint(-7,7)
            while a1**2+b1**2+c1**2==0 or a2==0 or b2==0 or c2==0 or a1*a2+b1*b2+c1*c2==0:
                a1=randint(-6,6)
                b1=randint(-6,6)
                c1=randint(-7,7)
                d1=randint(-15,15)
                a2=randint(-6,6)
                b2=randint(-6,6)
                c2=randint(-7,7)
                d2=randint(-15,15)
                xa=randint(-6,6)
                ya=randint(-6,6)
                za=randint(-7,7)
            pt1=a1*x+b1*y+c1*z+d1
            hd=x-xa
            td=y-ya
            cd=z-za
            tvh=abs(a1*a2+b1*b2+c1*c2)
            tv=a1*a2+b1*b2+c1*c2
            l1=sqrt(a1**2+b1**2+c1**2)
            l2=sqrt(a2**2+b2**2+c2**2)
            cos=nsimplify(tvh/(l1*l2))
            g=math.degrees(math.asin(cos))
            kq1=g
            kq2=g+2
            number = Decimal(float(kq1))  # Số cần làm tròn
            kq_1 = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
            number = Decimal(float(kq2))  # Số cần làm tròn
            kq_2 = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)


            # Nội dung câu hỏi
            noidungcauhoi = ('Trong không gian với hệ tọa độ $Oxyz$, cho đường thẳng $\\Delta: \\dfrac{%s}{%s}=\\dfrac{%s}{%s}=\\dfrac{%s}{%s}$ và mặt phẳng $(P):%s=0$. Xét các vectơ $\\vec{u}=(%s;%s;%s),\\vec{n}=(%s;%s;%s)$.'
                            %(latex(hd),latex(a2),latex(td),latex(b2),latex(cd),latex(c2),latex(pt1),
                            latex(a2),latex(b2),latex(c2),
                            latex(a1),latex(b1),latex(c1),
                            ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $\\vec{n}$ là một vectơ pháp tuyến của mặt phẳng $(P)$'
            nb_da_1_s = '$\\vec{n}$ không là một vectơ pháp tuyến của mặt phẳng $(P)$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('$\\vec{n}$ là một vectơ pháp tuyến của mặt phẳng $(P)$'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $\\vec{u}$ là một vectơ chỉ phương của đường thẳng $\\Delta$'
            th_da_1_s = '$\\vec{u}$ không là một vectơ chỉ phương của đường thẳng $\\Delta$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('$\\vec{u}$ là một vectơ chỉ phương của đường thẳng $\\Delta$.'

                        )


            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $\\vec{n}\\cdot\\vec{u}=%s$'%(latex(tv))
            vd_da_1_s = '$\\vec{n}_1\\cdot\\vec{n}_2=%s$'%(latex(tv+1))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True $\\sin \\left((P),\\Delta\\right)=%s$'%(latex(cos))
            vd_da_2_s = '$\\cos \\left((P),\\Delta\\right)=%s$'%(latex(nsimplify(cos)))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1,vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('Ta có $\\vec{n}\\cdot\\vec{u}=%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)=%s$.'

                            %(latex(a1),latex(a2),latex(b1),latex(b2),latex(c1),latex(c2),latex(tv)

                            )
                        )
            loigiai_vd_2 = ('Mặt phẳng $(P)$ có vectơ pháp tuyến là $\\vec{n}=(%s;%s;%s)$.\\\\ \n'
                        'Đường thẳng $\\Delta$ có vectơ chỉ phương là $\\vec{u}=(%s;%s;%s)$.\\\\ \n'
                        'Ta có $\\sin \\left((P),\\Delta\\right)=\\dfrac{\\abs{%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}\\cdot\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%s$.'

                    %(latex(a1),latex(b1),latex(c1),
                    latex(a2),latex(b2),latex(c2),
                    latex(a1),latex(a2),latex(b1),latex(b2),latex(c1),latex(c2),
                    latex(a1),latex(b1),latex(c1),
                    latex(a2),latex(b2),latex(c2),latex(cos)

                    ))


            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1,loigiai_vd_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Góc giữa đường thẳng $\\Delta$ và mặt phẳng $(P)$ bằng khoảng $%s^{\\circ}$ (làm tròn đến hàng đơn vị của độ)'%(latex(kq_1))
            vdc_da_1_s = 'Góc giữa đường thẳng $\\Delta$ và mặt phẳng $(P)$ bằng khoảng $%s^{\\circ}$ (làm tròn đến hàng đơn vị của độ)'%(latex(kq_2))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Mặt phẳng $(P)$ có vectơ pháp tuyến là $\\vec{n}=(%s;%s;%s)$.\\\\ \n'
                        'Đường thẳng $\\Delta$ có vectơ chỉ phương là $\\vec{u}=(%s;%s;%s)$.\\\\ \n'
                        'Ta có $\\sin \\left(\\Delta,(P)\\right)=\\dfrac{\\abs{%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}\\cdot\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%s$.\\\\ \n'
                        'Do đó $\\left(\\Delta,(P)\\right)\\approx %s^{\\circ}$.'
                    %(latex(a1),latex(b1),latex(c1),
                    latex(a2),latex(b2),latex(c2),
                    latex(a1),latex(a2),latex(b1),latex(b2),latex(c1),latex(c2),
                    latex(a1),latex(b1),latex(c1),
                    latex(a2),latex(b2),latex(c2),latex(cos),latex(kq_1)

                    ))


            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('--','+').replace('+-','-')
            return content

