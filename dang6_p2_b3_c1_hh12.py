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


def bt_dang6_p2_b3_c1_hh12(self):
            # Khai báo biến
            xa=randint(-8,8)
            ya=randint(-8,8)
            za=randint(-5,5)
            xb=randint(-6,6)
            yb=randint(-7,7)
            zb=randint(-5,6)
            xc=randint(-6,6)
            yc=randint(-7,7)
            zc=randint(-6,6)
            x1=xb-xa
            y1=yb-ya
            z1=zb-za
            x2=xc-xa
            y2=yc-ya
            z2=zc-za
            xn=y1*z2-z1*y2
            yn=z1*x2-x1*z2
            zn=x1*y2-y1*x2


            while xa==xb or ya==yb or za==zb or xn==0 or yn==0 or zn==0 or xn*xa+yn*ya+zn*za==0:
                xa=randint(-8,8)
                ya=randint(-8,8)
                za=randint(-5,5)
                xb=randint(-6,6)
                yb=randint(-7,7)
                zb=randint(-5,6)
                xc=randint(-6,6)
                yc=randint(-7,7)
                zc=randint(-6,6)
                x1=xb-xa
                y1=yb-ya
                z1=zb-za
                x2=xc-xa
                y2=yc-ya
                z2=zc-za
                xn=y1*z2-z1*y2
                yn=z1*x2-x1*z2
                zn=x1*y2-y1*x2
            l=sqrt(xn**2+yn**2+zn**2)
            s=nsimplify(l/2)
            xg=nsimplify((xa+xb+xc)/3)
            yg=nsimplify((ya+yb+yc)/3)
            zg=nsimplify((za+zb+zc)/3)
            xd=xc-xb+xa
            yd=yc-yb+ya
            zd=zc-zb+za
            x3=xc-xb
            y3=yc-yb
            z3=zc-zb
            dab=sqrt(x1**2+y1**2+z1**2)
            dac=sqrt(x2**2+y2**2+z2**2)
            dbc=sqrt(x3**2+y3**2+z3**2)
            ts=nsimplify(-za/z1)
            xi=nsimplify((-za/z1)*x1+xa)
            yi=nsimplify((-za/z1)*y1+ya)

            # Nội dung câu hỏi
            noidungcauhoi = ('Trong không gian $Oxyz$, cho tam giác $ABC$ với $A(%s;%s;%s), B(%s;%s;%s)$ và $C(%s;%s;%s)$.'
                            %(latex(xa),latex(ya),latex(za),latex(xb),latex(yb),latex(zb),latex(xc),latex(yc),latex(zc)))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Toạ độ trọng tâm của tam giác $ABC$ là $\\left(%s;%s;%s\\right)$'%(latex(xg),latex(yg),latex(zg))
            nb_da_1_s = 'Toạ độ trọng tâm của tam giác $ABC$ là $\\left(%s;%s;%s\\right)$'%(latex(xg),latex(yg),latex(zg+1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('Toạ độ trọng tâm của tam giác $ABC$ là $\\left(%s;%s;%s\\right)$.'%(latex(xg),latex(yg),latex(zg))
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
            th_da_1_d = '\\True Nếu tứ giác $ABCD$ là hình bình hành thì $D(%s;%s;%s)$'%(latex(xd),latex(yd),latex(zd))
            th_da_1_s = 'Nếu tứ giác $ABCD$ là hình bình hành thì $D(%s;%s;%s)$'%(latex(xd),latex(yd),latex(zd+2))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('Để tứ giác $ABCD$ là hình bình hành thì $\\vec{AD}=\\vec{BC}$.\\\\ \n'
                            'Theo bài ta có $\\vec{AD}=(x-%s;y-%s;z-%s)$ và $\\vec{BC}=(%s;%s;%s)$.\\\\ \n'
                            '\\hspace*{1cm}$\\vec{AD}=\\vec{BC} \\Leftrightarrow \\heva{x-%s=%s\\\\y-%s=%s\\\\z-%s=%s} \\Leftrightarrow \\heva{x=%s\\\\y=%s\\\\z=%s}$.\\\\ \n'
                            'Vậy $D(%s;%s;%s)$.'
                            %(latex(xa),latex(ya),latex(za),latex(xc-xb),latex(yc-yb),latex(zc-zb),latex(xa),latex(xc-xb),latex(ya),latex(yc-yb),latex(za),latex(zc-zb),
                            latex(xd),latex(yd),latex(zd),latex(xd),latex(yd),latex(zd))

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
            vd_da_1_d = '\\True Diện tích tam giác $ABC$ bằng $%s$'%(latex(s))
            vd_da_1_s = 'Diện tích tam giác $ABC$ bằng $%s$'%(latex(2*s))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('Ta có \\\\ \n'
                            '$\\vec{AB}=(%s;%s;%s)\\Rightarrow c=AB=\\abs{\\vec{AB}}=\\sqrt{(%s)^2+(%s)^2+(%s)^2}=%s$.\\\\ \n'
                            '$\\vec{AC}=(%s;%s;%s)\\Rightarrow b=AC=\\abs{\\vec{AC}}=\\sqrt{(%s)^2+(%s)^2+(%s)^2}=%s$.\\\\ \n'
                            '$\\vec{BC}=(%s;%s;%s)\\Rightarrow c=BC=\\abs{\\vec{BC}}=\\sqrt{(%s)^2+(%s)^2+(%s)^2}=%s$.\\\\ \n'
                            'Suy ra $p=\\dfrac{a+b+c}{2}=\\dfrac{%s+%s+%s}{2}$.\\\\ \n'
                            'Diện tích tam giác $ABC$ tính theo công thức Heron là\\\\ \n'
                            '$S=\\sqrt{p(p-a)(p-b)(p-c)}=%s$.'
                            %(latex(x1),latex(y1),latex(z1),latex(x1),latex(y1),latex(z1),latex(dab),
                            latex(x2),latex(y2),latex(z2),latex(x2),latex(y2),latex(z2),latex(dac),
                            latex(x3),latex(y3),latex(z3),latex(x3),latex(y3),latex(z3),latex(dbc),
                            latex(dbc),latex(dac),latex(dab),latex(s)

                            )
                        )


            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Toạ độ giao điểm của đường thẳng $AB$ với mặt phẳng $(Oxy)$ là $\\left(%s;%s;0\\right)$'%(latex(xi),latex(yi))
            vdc_da_1_s = 'Toạ độ giao điểm của đường thẳng $AB$ với mặt phẳng $(Oxy)$ là $\\left(%s;%s;1\\right)$'%(latex(xi),latex(yi))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)



            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Gọi $I(x;y;0)$ là giao điểm của đường thẳng $AB$ với mặt phẳng $(Oxy)$ khi đó ta có ba điểm $A,B,I$ thẳng hàng, do đó hai vectơ $\\vec{AI},\\vec{AB}$ cùng phương. \\\\ \n'
                            'Suy ra\\\\ \n'
                            '$\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{-%s}{%s}\\Rightarrow \\heva{&x=%s\\\\&y=%s}.$\\\\ \n'
                            'Vậy $I\\left(%s;%s;0\\right)$.'
                            %(latex(xa),latex(x1),latex(ya),latex(y1),latex(za),latex(z1),
                            latex(xi),latex(yi),latex(xi),latex(yi)
                                )
                        )

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

