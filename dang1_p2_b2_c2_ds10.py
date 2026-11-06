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


def bt_dang1_p2_b2_c2_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x = symbols('x')
                y = symbols('y')
                listen1=['Hưng','Bình','Mạnh','Kha','Phi','Việt','Tuyên','Đại','Hải','Hòa','Lâm','Tuấn','Trường','Sơn','Nam','Thắng','Dương','Đức','Hùng','Dũng']
                ten=random.choice(listen1)

                a1=randint(20,50)
                a=a1*10

                b1=randint(5,10)
                b=b1*10
                k=randint(2,5)

                x01=randint(20,50)
                x0=x01*10
                y01=randint(5,10)
                y0=y01*10

                x11=randint(30,50)
                x1=x11*10
                y11=randint(5,10)
                y1=y11*10

                x21=randint(20,40)
                x2=x21*10
                y21=randint(20,30)
                y2=y21*10


                while 5*k>=a or x0+y0>a or y0<b or x0<k*y0 or x1+y1<a or x2>k*y2:

                    a1=randint(20,50)
                    a=a1*10

                    b1=randint(5,10)
                    b=b1*10
                    k=randint(2,5)

                    x01=randint(20,50)
                    x0=x01*10
                    y01=randint(5,10)
                    y0=y01*10

                    x11=randint(20,40)
                    x1=x11*10
                    y11=randint(5,10)
                    y1=y11*10

                    x21=randint(20,40)
                    x2=x21*10
                    y21=randint(20,30)
                    y2=y21*10

                y3=Rational(a,k+1)
                x3=a-y3
            # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd(a,b),1)
            # Rút gọn các hệ số
                hs_a1 =a // gcd
                hs_b1 =b // gcd
                hs_c1 =1 // gcd
            #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                xc = hs_a1*x+hs_b1*y<=hs_c1


                # Nội dung câu hỏi
                noidungcauhoi = ('Bác %s có kế hoạch đầu tư không quá $%s$ triệu đồng vào hai khoản $X$ và khoản $Y$. '
                                'Để đạt được lợi nhuận thì khoản $Y$ phải đầu tư ít nhất $%s$ triệu đồng và số tiền đầu tư '
                                'cho khoản $X$ phải ít nhất gấp $%s$ lần số tiền cho khoản $Y$. '
                                %(str(ten),latex(a),latex(b),latex(k)
                                ))



                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Gọi $x,y$ (đơn vị triệu đồng) lần lượt là tiền bác %s đầu từ vào $X$ và $Y$. Khi đó, để bác %s có lợi nhuận thì $x, y$ phải thỏa mãn hệ bất phương trình $\\heva{&x+y\\le %s \\\\& y\\ge %s\\\\ & x\\ge %s y}$'%(str(ten),str(ten),latex(a),latex(b),latex(k))
                nb_da_1_s = 'Gọi $x,y$ (đơn vị triệu đồng) lần lượt là tiền bác %s đầu từ vào $X$ và $Y$. Khi đó, để bác %s có lợi nhuận thì $x, y$ phải thỏa mãn hệ bất phương trình $\\heva{&x+y\\le %s \\\\& y\\ge %s\\\\ & x\\le %s y}$'%(str(ten),str(ten),latex(a),latex(b),latex(k))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True Gọi $x,y$ (đơn vị triệu đồng) lần lượt là tiền bác %s đầu từ vào $X$ và $Y$. Khi đó ta có hệ phương trình $\\heva{&x+y\\le %s \\\\& y\\ge %s\\\\ & x\\ge %s y}$'%(str(ten),latex(a),latex(b),latex(k))
                nb_da_2_s = 'Gọi $x,y$ (đơn vị triệu đồng) lần lượt là tiền bác %s đầu từ vào $X$ và $Y$. Khi đó ta có hệ phương trình $\\heva{&x+y< %s \\\\& y\\ge %s\\\\ & x\\ge %s y}$'%(str(ten),latex(a),latex(b),latex(k))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]

                nb_da_2=random.choice(list_nb_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2]

                # Nội dung lời giải
                loigiai_nb_1 = ('Gọi $x,y$ (đơn vị triệu đồng) lần lượt là tiền bác %s đầu từ vào $X$ và $Y$. Khi đó ta có hệ phương trình $\\heva{&x+y\\le %s \\\\& y\\ge %s\\\\ & x\\ge %s y}$. '
                                %(str(ten),latex(a),latex(b),latex(k)))
                loigiai_nb_2 = ('Gọi $x,y$ (đơn vị triệu đồng) lần lượt là tiền bác %s đầu từ vào $X$ và $Y$. Khi đó ta có hệ phương trình $\\heva{&x+y\\le %s \\\\& y\\ge %s\\\\ & x\\ge %s y}$. '
                                %(str(ten),latex(a),latex(b),latex(k)))
                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Miền nghiệm của hệ bất phương trình tiền bác %s đầu tư là một tam giác'%(str(ten))
                th_da_1_s = 'Miền nghiệm của hệ bất phương trình tiền bác %s đầu tư là một tứ giác'%(str(ten))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                th_da_2_d = '\\True Miền nghiệm của hệ bất phương trình tiền bác %s đầu tư là một tam giác'%(str(ten))
                th_da_2_s = 'Miền nghiệm của hệ bất phương trình tiền bác %s đầu tư là một hình vuông'%(str(ten))
                list_th_da_2=[th_da_2_d,th_da_2_s]

                th_da_2=random.choice(list_th_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1, th_da_2]

                # Nội dung lời giải
                loigiai_th_1 = ('Biểu diễn miền nghiệm của hệ bất phương trình tiền bác %s đầu tư là một tam giác.'
                                %(str(ten),
                                ))
                loigiai_th_2 = ('Biểu diễn miền nghiệm của hệ bất phương trình tiền bác %s đầu tư là một tam giác.'
                                %(str(ten),
                                ))
                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1, loigiai_th_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Điểm $(%s;%s)$ thuộc miền nghiệm của hệ bất phương trình tiền bác %s đầu tư vào hai khoản $X,Y$ có lợi nhuận'%(latex(x0),latex(y0),str(ten))
                vd_da_1_s = 'Điểm $(%s;%s)$ thuộc miền nghiệm của hệ bất phương trình tiền bác %s đầu tư vào hai khoản $X,Y$ có lợi nhuận'%(latex(x1),latex(y1),str(ten))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True Điểm $(%s;%s)$ thuộc miền nghiệm của hệ bất phương trình tiền bác %s đầu tư vào hai khoản $X,Y$ có lợi nhuận'%(latex(x0),latex(y0),str(ten))
                vd_da_2_s = 'Điểm $(%s;%s)$ thuộc miền nghiệm của hệ bất phương trình tiền bác %s đầu tư vào hai khoản $X,Y$ có lợi nhuận'%(latex(x2),latex(y2),str(ten))
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]

                vd_da_2=random.choice(list_vd_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1, vd_da_2]

                # Nội dung lời giải
                # Nội dung lời giải
                loigiai_vd_1 = ('Ta có $(%s;%s)$ thỏa mãn cả ba bất phương trình nên cặp số $(%s;%s)$ thuộc miền nghiệm tiền bác %s đầu tư vào hai khoản $X,Y$ có lợi nhuận.\\\\ \n'
                                ' $(%s;%s)$ không thỏa mãn bất phương trình $x+y\\le %s$ của hệ nên cặp số $(%s;%s)$ không thuộc miền nghiệm tiền bác %s đầu tư vào hai khoản $X,Y$ có lợi nhuận.'
                                %(latex(x0),latex(y0),latex(x0),latex(y0),str(ten),
                                latex(x1),latex(y1),latex(a),latex(x1),latex(y1),str(ten),
                                ))
                loigiai_vd_2 = ('Ta có $(%s;%s)$ thỏa mãn cả ba bất phương trình nên cặp số $(%s;%s)$ thuộc miền nghiệm tiền bác %s đầu tư vào hai khoản $X,Y$ có lợi nhuận.\\\\ \n'
                                ' $(%s;%s)$ không thỏa mãn bất phương trình $x\\ge%s y$ của hệ nên cặp số $(%s;%s)$ không thuộc miền nghiệm tiền bác %s đầu tư vào hai khoản $X,Y$ có lợi nhuận.'
                                %(latex(x0),latex(y0),latex(x0),latex(y0),str(ten),
                                latex(x2),latex(y2),latex(k),latex(x2),latex(y2),str(ten),
                                ))

                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d = '\\True Điểm $A(%s;%s)$ là điểm có tung độ lớn nhất thuộc miền nghiệm của hệ bất phương trình tiền bác %s đầu tư có lợi nhuận.'%(latex(x3),latex(y3), str(ten))
                vdc_da_1_s = 'Điểm $B(%s;%s)$ là điểm có tung độ lớn nhất thuộc miền nghiệm của hệ bất phương trình tiền bác %s đầu tư có lợi nhuận.'%(latex(3*b),latex(b), str(ten))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Điểm $A(%s;%s)$ là điểm có tung độ lớn nhất thuộc miền nghiệm của hệ bất phương trình tiền bác %s đầu tư có lợi nhuận.'%(latex(x3),latex(y3), str(ten))
                vdc_da_2_s = 'Điểm $C(%s;%s)$ là điểm có tung độ lớn nhất thuộc miền nghiệm của hệ bất phương trình tiền bác %s đầu tư có lợi nhuận.'%(latex(a-b),latex(b), str(ten))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

                vdc_da_2=random.choice(list_vdc_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2]

                # Nội dung lời giải
                loigiai_vdc_1 =('Miền nghiệm của bất phương trình là hình tam giác đỉnh $A$ đáy $BC$ nằm trên đường thẳng song song với trục $Ox$.\\\\ \n'
                                'Với $A(%s;%s)$ và $B(%s;%s);C(%s;%s)$.'
                                %(latex(x3),latex(y3),latex(k*b),latex(b),latex(a-b),latex(b),
                                ))
                loigiai_vdc_2 =('Miền nghiệm của bất phương trình là hình tam giác đỉnh $A$ đáy $BC$ nằm trên đường thẳng song song với trục $Ox$.\\\\ \n'
                                'Với $A(%s;%s)$ và $B(%s;%s);C(%s;%s)$.'
                                %(latex(x3),latex(y3),latex(k*b),latex(b),latex(a-b),latex(b),
                                ))
                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

